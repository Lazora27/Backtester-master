import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DPOCycles': 1.0
        })
    )
