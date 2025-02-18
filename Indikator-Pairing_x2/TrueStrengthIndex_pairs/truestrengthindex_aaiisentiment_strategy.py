import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
