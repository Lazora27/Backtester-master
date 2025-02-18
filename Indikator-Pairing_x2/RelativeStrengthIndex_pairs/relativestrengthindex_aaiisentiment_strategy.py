import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
