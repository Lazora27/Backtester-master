import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
