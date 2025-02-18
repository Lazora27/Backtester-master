import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
