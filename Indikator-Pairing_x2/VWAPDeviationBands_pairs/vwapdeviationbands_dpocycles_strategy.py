import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'DPOCycles': 1.0
        })
    )
