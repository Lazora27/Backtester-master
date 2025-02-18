import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
