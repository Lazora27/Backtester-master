import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
