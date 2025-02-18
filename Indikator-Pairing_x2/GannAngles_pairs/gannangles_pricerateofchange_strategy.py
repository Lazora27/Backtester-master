import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
