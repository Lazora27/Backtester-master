import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
