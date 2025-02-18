import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'EhlersDecycler': 1.0
        })
    )
