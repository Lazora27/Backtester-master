import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'BuyingPressure': 1.0
        })
    )
