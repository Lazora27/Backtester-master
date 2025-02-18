import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
