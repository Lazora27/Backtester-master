import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und TimeCycle
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'TimeCycle': 1.0
        })
    )
