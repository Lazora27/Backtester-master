import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
