import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
