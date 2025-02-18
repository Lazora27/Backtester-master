import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
