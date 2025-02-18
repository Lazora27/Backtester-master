import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und GannFans
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'GannFans': 1.0
        })
    )
