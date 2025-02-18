import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
