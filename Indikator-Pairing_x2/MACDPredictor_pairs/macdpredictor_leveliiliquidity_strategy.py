import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
