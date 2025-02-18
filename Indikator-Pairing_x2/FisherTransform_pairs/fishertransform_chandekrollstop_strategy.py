import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
