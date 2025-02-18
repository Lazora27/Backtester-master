import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'CyberCycle': 1.0
        })
    )
