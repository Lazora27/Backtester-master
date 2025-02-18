import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TrendCycles': 1.0
        })
    )
