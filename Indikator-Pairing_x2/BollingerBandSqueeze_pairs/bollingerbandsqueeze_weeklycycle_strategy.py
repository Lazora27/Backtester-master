import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'WeeklyCycle': 1.0
        })
    )
