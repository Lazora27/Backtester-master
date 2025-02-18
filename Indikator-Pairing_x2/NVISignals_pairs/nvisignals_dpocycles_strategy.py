import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DPOCycles
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DPOCycles': 1.0
        })
    )
