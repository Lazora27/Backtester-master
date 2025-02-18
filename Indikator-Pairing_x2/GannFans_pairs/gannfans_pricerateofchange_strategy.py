import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
