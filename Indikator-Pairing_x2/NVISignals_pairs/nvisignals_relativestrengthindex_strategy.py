import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
