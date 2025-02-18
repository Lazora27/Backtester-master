import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
