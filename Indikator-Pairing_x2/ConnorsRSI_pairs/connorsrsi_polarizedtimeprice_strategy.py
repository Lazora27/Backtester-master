import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
