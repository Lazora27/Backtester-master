import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
