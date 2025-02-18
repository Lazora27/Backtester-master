import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'TrendCycles': 1.0
        })
    )
