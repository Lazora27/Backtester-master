import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'VWAPBands': 1.0
        })
    )
