import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BollingerBands': 1.0
        })
    )
