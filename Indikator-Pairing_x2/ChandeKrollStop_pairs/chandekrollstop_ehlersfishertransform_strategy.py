import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
