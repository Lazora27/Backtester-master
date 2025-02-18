import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'WeeklyCycle': 1.0
        })
    )
