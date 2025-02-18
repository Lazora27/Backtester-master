import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'UltimateOscillator': 1.0
        })
    )
