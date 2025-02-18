import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DPOCycles': 1.0
        })
    )
