import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AAIISentiment': 1.0
        })
    )
