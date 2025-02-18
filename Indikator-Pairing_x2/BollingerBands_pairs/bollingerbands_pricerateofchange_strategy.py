import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
