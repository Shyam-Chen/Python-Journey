import * as ort from 'onnxruntime-node';

// ========== 預測資料 ==========
const months = Array.from({ length: 12 }, (_, i) => i + 1); // [1, 2, ..., 12]
const projectCounts = [0, 0, 0, 6, 15, 11, 0, 2, 0, 0, 0, 3];
const projectDensity = months.map((m, i) => projectCounts[i] / m); // 專案密度

// ✅ 將三個特徵展平成一維 Float64Array，shape: (12, 3)
//    對應 Python 的 X_2026.to_numpy().astype(np.float64)
const rows = 12;
const cols = 3; // 月份、專案數量、專案密度
const inputData = new Float64Array(rows * cols);

for (let i = 0; i < rows; i++) {
  inputData[i * cols + 0] = months[i];
  inputData[i * cols + 1] = projectCounts[i];
  inputData[i * cols + 2] = projectDensity[i];
}

// ========== 執行推理 ==========
async function main() {
  const session = await ort.InferenceSession.create('model.onnx', {
    executionProviders: ['cpu'],
  });

  const inputName = session.inputNames[0];

  // ✅ 對應 Python 的 np.float64 → 使用 'float64' + Float64Array
  const tensor = new ort.Tensor('float64', inputData, [rows, cols]);

  const results = await session.run({ [inputName]: tensor });
  const outputName = session.outputNames[0];

  // ✅ 對應 Python 的 pred.flatten()
  //    onnxruntime-node 的 .data 本身就是一維 Float64Array
  const pred = Array.from(results[outputName].data as Float64Array);

  // ========== 整理結果 ==========
  const predictions = pred.map((v) => Math.round(v));

  console.log('='.repeat(50));
  console.log('2026 年預測結果：');
  console.log('='.repeat(50));
  console.log('月份 | 專案數量 | 預測工單_線性迴歸');
  console.log('-'.repeat(35));

  for (let i = 0; i < rows; i++) {
    console.log(
      `${String(months[i]).padStart(4)} | ${String(projectCounts[i]).padStart(8)} | ${predictions[i]}`,
    );
  }

  const total = predictions.reduce((a, b) => a + b, 0);
  console.log('\n' + '='.repeat(50));
  console.log('2026 年度總計預測：');
  console.log('='.repeat(50));
  console.log(`線性迴歸預測總工單數: ${total} 張`);
}

main().catch(console.error);
