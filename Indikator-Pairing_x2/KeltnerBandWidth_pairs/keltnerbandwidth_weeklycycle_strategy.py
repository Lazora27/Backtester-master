import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'WeeklyCycle': 1.0
        })
    )
