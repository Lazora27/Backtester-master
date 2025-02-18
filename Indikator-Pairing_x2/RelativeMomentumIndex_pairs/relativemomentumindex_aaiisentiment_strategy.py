import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'AAIISentiment': 1.0
        })
    )
