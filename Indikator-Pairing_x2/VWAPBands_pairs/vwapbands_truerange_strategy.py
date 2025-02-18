import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TrueRange
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TrueRange': 1.0
        })
    )
