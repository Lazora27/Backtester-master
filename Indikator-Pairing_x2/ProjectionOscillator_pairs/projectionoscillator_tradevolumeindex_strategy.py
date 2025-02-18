import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
