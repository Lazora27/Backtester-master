import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
