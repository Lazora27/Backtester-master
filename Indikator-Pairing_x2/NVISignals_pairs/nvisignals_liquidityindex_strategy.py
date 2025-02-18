import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'LiquidityIndex': 1.0
        })
    )
