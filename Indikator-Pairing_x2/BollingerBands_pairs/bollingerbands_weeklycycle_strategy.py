import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'WeeklyCycle': 1.0
        })
    )
