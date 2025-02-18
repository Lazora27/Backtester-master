import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
