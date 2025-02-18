import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
