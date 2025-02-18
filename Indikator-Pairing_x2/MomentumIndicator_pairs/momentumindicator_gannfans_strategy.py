import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und GannFans
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'GannFans': 1.0
        })
    )
