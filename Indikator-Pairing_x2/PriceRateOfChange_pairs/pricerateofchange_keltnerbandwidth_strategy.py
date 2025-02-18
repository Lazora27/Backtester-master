import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
