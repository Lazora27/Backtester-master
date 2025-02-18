import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
