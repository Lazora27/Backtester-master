import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und TrendCycles
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'TrendCycles': 1.0
        })
    )
